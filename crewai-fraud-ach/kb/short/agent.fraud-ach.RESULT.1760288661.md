```json
{
  "id": "74cf3fee1a18cec4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288661,
  "host_pid": "9e6742732c60:1",
  "hash": "c71c11db61893a4781ed4b63df370e6bb57300ae776e6b4ffe880193160d1285",
  "cid": "QmV1c71c11db61893a4781ed4b63df370e6bb57300ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288661,
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
      "evaluated_at": 1760288661
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
  "sig": "5741e57e30aad5aeef51748a33717b7286635a4f21d9901238e61de69ba5dba0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272560065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 20112224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}