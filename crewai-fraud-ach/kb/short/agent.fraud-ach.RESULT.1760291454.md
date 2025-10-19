```json
{
  "id": "c223e0f838035615",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291454,
  "host_pid": "9e6742732c60:1",
  "hash": "d7cbf179a4a3e5cb5f8001d7d71a5d5b3edf99e5a505465a554b2f0c1d45bbdb",
  "cid": "QmV1d7cbf179a4a3e5cb5f8001d7d71a5d5b3edf99e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291454,
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
      "evaluated_at": 1760291454
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
  "sig": "a8972f24dce0e855cdcc07de5f40db9ffbff2d5cbc6b4be6d3c3f7fbccf0656e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 22262275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}