```json
{
  "id": "e6c56873e34376d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287360,
  "host_pid": "9e6742732c60:1",
  "hash": "3923e06b677a3df929d15069e07d86794318a82ee4a0c648b9c927d4996abe3c",
  "cid": "QmV13923e06b677a3df929d15069e07d86794318a82e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287360,
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
      "evaluated_at": 1760287360
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
  "sig": "b3718a919c7c5b5bdfd3f82451848f1770ac8466fe23009e9968d07220301a2f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 26150973, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}