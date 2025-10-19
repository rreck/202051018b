```json
{
  "id": "db4adc4b346ca73c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288205,
  "host_pid": "9e6742732c60:1",
  "hash": "567ce39a15bb764aaf581f976bd00167b60a4f2adbac60d811037f3b3f5dcc88",
  "cid": "QmV1567ce39a15bb764aaf581f976bd00167b60a4f2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288205,
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
      "evaluated_at": 1760288205
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
  "sig": "93291527ed583339be747659cffd951e1c91a3336c805535dbe4a5ab54e4bdf0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 503193792297075
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 35963824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}