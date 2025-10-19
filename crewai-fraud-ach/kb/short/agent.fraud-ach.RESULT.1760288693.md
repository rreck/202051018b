```json
{
  "id": "936608f07b4d8082",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288693,
  "host_pid": "9e6742732c60:1",
  "hash": "af739ae59fe7563f21a92b37361acacd31f3f317746a7675d46ae7ac9e4c8cb7",
  "cid": "QmV1af739ae59fe7563f21a92b37361acacd31f3f317",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288693,
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
      "evaluated_at": 1760288693
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
  "sig": "2f5999f2e3edfe4c75e8e22ae9d1ce2f55aebd1ad1c1964624f4856eaf7a423f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 31533008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}