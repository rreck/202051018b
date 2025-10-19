```json
{
  "id": "9a8cc2606aa85172",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286703,
  "host_pid": "9e6742732c60:1",
  "hash": "69e4df33af9ffc5f2b7d27dce32115c15b7774a6d3debfc7bb83c4258ec8c4fe",
  "cid": "QmV169e4df33af9ffc5f2b7d27dce32115c15b7774a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286703,
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
      "evaluated_at": 1760286703
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "123f8ec59fda6292cb42a2fc5609f53c5dc990930a9342d9ff12432bf5414d5d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15235366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}