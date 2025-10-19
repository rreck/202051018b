```json
{
  "id": "a0e1a802b592a739",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292805,
  "host_pid": "9e6742732c60:1",
  "hash": "9d766b20d788db8c747ab91fe62813e35eca60546fc7627f9aa52a85d2c18a66",
  "cid": "QmV19d766b20d788db8c747ab91fe62813e35eca6054",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292805,
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
      "evaluated_at": 1760292805
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
  "sig": "9db295cc6684aaef08720178eb30b9be2dc523f24a0b3a4ec23593f33d1351a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038907358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 44336375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '4f1b5532b664e41d'}}}