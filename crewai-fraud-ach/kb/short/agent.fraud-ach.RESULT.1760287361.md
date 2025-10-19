```json
{
  "id": "ec0e1836d4675259",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287361,
  "host_pid": "9e6742732c60:1",
  "hash": "12a1b23a88bd0b798c060d31a3f62ea39ffb8176bd1e32f3aa2ceb73fac8177a",
  "cid": "QmV112a1b23a88bd0b798c060d31a3f62ea39ffb8176",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287361,
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
      "evaluated_at": 1760287361
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
  "sig": "04b5e29891ef5c11575a8ece675d3c48d1e88fa591dfe12bea6377d86ac9ccd4"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 17875998, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}