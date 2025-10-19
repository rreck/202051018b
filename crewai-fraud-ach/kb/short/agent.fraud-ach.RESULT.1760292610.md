```json
{
  "id": "76406268a26eba75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292610,
  "host_pid": "9e6742732c60:1",
  "hash": "6941d919e80c2d7a573c20f9da8a7d16a96b0451b2570105738b7f56c8ee1b1f",
  "cid": "QmV16941d919e80c2d7a573c20f9da8a7d16a96b0451",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292610,
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
      "evaluated_at": 1760292610
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
  "sig": "550c2ee625b903a0d8e1229727d9a99c39f9447d702316cee568a7e2df2fbcca"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 80210457, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}