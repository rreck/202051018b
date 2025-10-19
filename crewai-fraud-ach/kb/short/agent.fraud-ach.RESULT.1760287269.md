```json
{
  "id": "16d2bbf3fff2efce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287269,
  "host_pid": "9e6742732c60:1",
  "hash": "7994c1f23c281710a59f2daeda307e33b1cf3c54dee4ccb7a00242f959836a21",
  "cid": "QmV17994c1f23c281710a59f2daeda307e33b1cf3c54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287269,
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
      "evaluated_at": 1760287269
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
  "sig": "1370c291fef1dfa75b633596afcb5734e0b26c1d98d2c1fe64ad86338b87a2d4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000245693870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 13888638, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': '3f6bcdf181d34e46'}}}f9d'}}}