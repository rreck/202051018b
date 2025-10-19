```json
{
  "id": "29eda1c1d47c6193",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290162,
  "host_pid": "9e6742732c60:1",
  "hash": "51730a3b35af83c19db9c97a62a95ab74e47c835ba58c221118e4f57c17bccb3",
  "cid": "QmV151730a3b35af83c19db9c97a62a95ab74e47c835",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290162,
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
      "evaluated_at": 1760290162
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
  "sig": "632627ab83d62837abc65429edde35b8493bbfee2b8dd297f3fbb3b934c41537"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 69911556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}