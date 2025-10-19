```json
{
  "id": "48d2f41ca04ea6c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292463,
  "host_pid": "9e6742732c60:1",
  "hash": "ada9e901b868f81d19d03079f356ef9a801e514fea4b1b5d0cd1d52b01ed2817",
  "cid": "QmV1ada9e901b868f81d19d03079f356ef9a801e514f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292463,
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
      "evaluated_at": 1760292463
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
  "sig": "2afb73ee5899cd1515a86b15e717c8d7707866a5b1df319f73c724a8bb721e03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279947961
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 17061066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '22db2c62b181c93f'}}}