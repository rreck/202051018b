```json
{
  "id": "2542b8dcf0e0ecfa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287571,
  "host_pid": "9e6742732c60:1",
  "hash": "8e8e2e56ff8c51ee2224e0608de1ce0ceffdbe85b747cf9e2e4cb2caeebecf69",
  "cid": "QmV18e8e2e56ff8c51ee2224e0608de1ce0ceffdbe85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287571,
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
      "evaluated_at": 1760287571
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
  "sig": "cbc9f8423348e9772a09290090a90161e60bef91340372d94d17a208ccde59c8"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 111000026299785
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 28574715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'dc2585930aebf220'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}ower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306664}}}