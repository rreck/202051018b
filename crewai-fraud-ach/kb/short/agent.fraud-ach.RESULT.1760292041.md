```json
{
  "id": "397fa5bf00702192",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292041,
  "host_pid": "9e6742732c60:1",
  "hash": "b072695cde5b327766373905e739cefe9fac3042a7a0ed50fbc320249fb6eff6",
  "cid": "QmV1b072695cde5b327766373905e739cefe9fac3042",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292041,
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
      "evaluated_at": 1760292041
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
  "sig": "0c90eff8b43f9e7b0d00fd47555b97f9d81350ee5db2cf7dd6bef00530b31840"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246128124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 47250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'd8f9033e4ee0a57f'}}}