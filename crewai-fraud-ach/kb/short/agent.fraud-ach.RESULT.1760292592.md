```json
{
  "id": "2f5a1f1c4dc87577",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292592,
  "host_pid": "9e6742732c60:1",
  "hash": "eb6bfc8af4a00090161be820181bf7d545bb7c71312d6be96068fd921da51d0f",
  "cid": "QmV1eb6bfc8af4a00090161be820181bf7d545bb7c71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292592,
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
      "evaluated_at": 1760292592
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
  "sig": "571760ed4c81e83f664056b41dc37bd006ff4c9c7f92121553b128ed38044899"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 15373686, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}