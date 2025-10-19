```json
{
  "id": "a9e783763dac41f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293826,
  "host_pid": "9e6742732c60:1",
  "hash": "b17a14fecfbab210562ea25512ba27691e812dd7080eef6bd0f647ae8e935ce4",
  "cid": "QmV1b17a14fecfbab210562ea25512ba27691e812dd7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293826,
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
      "evaluated_at": 1760293826
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
  "sig": "713d8858442dbf402bb7901eb1508a5a253c9ee0898bc94bbc618786b36f7a10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 302, 'threshold': 50, 'total_amount': 20863066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 301, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}