```json
{
  "id": "51df6e0f540f3acf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292159,
  "host_pid": "9e6742732c60:1",
  "hash": "e894ce1fb1df17c8bb6b2b38447612348f606a8979749a0d1da26df7bc76191d",
  "cid": "QmV1e894ce1fb1df17c8bb6b2b38447612348f606a89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292159,
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
      "evaluated_at": 1760292159
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
  "sig": "54dbcb4789705eaf86e42e67d861579ee9492035d76cb7517fd0cd366a1d23bb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 64678139, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}