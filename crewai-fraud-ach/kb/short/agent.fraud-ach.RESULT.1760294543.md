```json
{
  "id": "6f2b5ccf3d5f31be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294543,
  "host_pid": "9e6742732c60:1",
  "hash": "2dbcbb3beff1f01f1c18fcbec21ac980c9c58b03b7fbd30357e79d29f92f9e31",
  "cid": "QmV12dbcbb3beff1f01f1c18fcbec21ac980c9c58b03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294543,
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
      "evaluated_at": 1760294543
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
  "sig": "adbd16b28643fb3a67882ff154d54fe0a71fbc32b623e2926cffd9aefa6ea546"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021151885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 58771440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}