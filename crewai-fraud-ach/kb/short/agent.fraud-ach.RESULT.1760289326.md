```json
{
  "id": "db5f64a9addd9ef3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289326,
  "host_pid": "9e6742732c60:1",
  "hash": "74e1ec55d7df3cb962a34b13fec0a0070c16924dbb9b945b9549e9046f6bd896",
  "cid": "QmV174e1ec55d7df3cb962a34b13fec0a0070c16924d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289326,
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
      "evaluated_at": 1760289326
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
  "sig": "d85feca383f562e172e742ed9a56ac503f92ac047c3dae79ddea7b8174c4b197"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 691661796885470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 12342240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285764, 'matching_hash': 'c2d09785100b76ca'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}