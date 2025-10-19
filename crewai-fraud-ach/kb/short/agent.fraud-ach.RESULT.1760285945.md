```json
{
  "id": "bc1cbe2e49292a03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285945,
  "host_pid": "9e6742732c60:1",
  "hash": "86eb289069fe317fc5cf3826e7795ef476551b0702b1f610f2b377f296cac862",
  "cid": "QmV186eb289069fe317fc5cf3826e7795ef476551b07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285945,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760285945
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "47778b5cc1fbf69c1786a2987486b473cbe8865528d6620893580cfae527cec0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242027891
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}