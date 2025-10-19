```json
{
  "id": "ed200876a50edc08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293024,
  "host_pid": "9e6742732c60:1",
  "hash": "bb476bde587da06cbd20527d1082b1cf4e31a34fa18cc70281aeb9958a9f3f6a",
  "cid": "QmV1bb476bde587da06cbd20527d1082b1cf4e31a34f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293024,
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
      "evaluated_at": 1760293024
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
  "sig": "0f287e4e30a78db5133c2419ecbcdffa9199f37a450ada0fee90d8f04a2639d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028364021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 10530660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'f023f2061dd68ffa'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}