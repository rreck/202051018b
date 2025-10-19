```json
{
  "id": "60cf758379ceac23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288570,
  "host_pid": "9e6742732c60:1",
  "hash": "bcfd4777d3184fb554c9938d10fd59c000bf57f97cfcdde86d8efdbd7265295c",
  "cid": "QmV1bcfd4777d3184fb554c9938d10fd59c000bf57f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288570,
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
      "evaluated_at": 1760288570
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "66719a06fce9526fdbcf27994d2768d93645d63d953a536f5a0f5bc7bffc6b92"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 595485910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6139030}}}