```json
{
  "id": "24a2c009a90c1bec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292016,
  "host_pid": "9e6742732c60:1",
  "hash": "58f38f3b634cbae88d8762cb53c191fb7abec4438e0745e5b3fc6dc870e802bb",
  "cid": "QmV158f38f3b634cbae88d8762cb53c191fb7abec443",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292016,
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
      "evaluated_at": 1760292016
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
  "sig": "64313d154ac6d1ca4e39e50500ba671381e66c48ba76b5cca8d07931bdc1f9f6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 906924177607497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 48502308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}