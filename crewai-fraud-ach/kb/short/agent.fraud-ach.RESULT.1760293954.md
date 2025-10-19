```json
{
  "id": "d37d4fd4153271d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293954,
  "host_pid": "9e6742732c60:1",
  "hash": "1a85c594afecf3f54f1eb17fd84084bea1c49a59924aa9c63ee74ed984507f0a",
  "cid": "QmV11a85c594afecf3f54f1eb17fd84084bea1c49a59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293954,
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
      "evaluated_at": 1760293954
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
  "sig": "f511744257879e17d99b8356e796b830c62208d8964d583905d8541daccb1e25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228343
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 22900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '964edcfaddb10414'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}