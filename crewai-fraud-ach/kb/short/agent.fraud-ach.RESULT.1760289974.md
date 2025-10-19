```json
{
  "id": "d113a2d6c03503cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289974,
  "host_pid": "9e6742732c60:1",
  "hash": "7004083b9b9715330a41b87d28d7fdffa737c8f9b581a9bf4acbfdf33c31c8fb",
  "cid": "QmV17004083b9b9715330a41b87d28d7fdffa737c8f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289974,
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
      "evaluated_at": 1760289974
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
  "sig": "667ed0e7f384038cf798786c00c28fd3796db07189004d64257511746001b0ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591169500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 27433434, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '9cbc2ba8ece9eaee'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}