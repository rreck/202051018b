```json
{
  "id": "a25c51fa057f99ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289087,
  "host_pid": "9e6742732c60:1",
  "hash": "23d74e8e83dd3c2f7dffbc45ee072aa94a9c1988d9f67043e1d11f79fa848382",
  "cid": "QmV123d74e8e83dd3c2f7dffbc45ee072aa94a9c1988",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289087,
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
      "evaluated_at": 1760289087
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "ece61824c9301461777c718ab85b8c50339174ff00fac8729752eba41eb620c9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 728187407566692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 52861965, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': '1da2d57caa7d5158'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}