```json
{
  "id": "69dac1211b22b936",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286392,
  "host_pid": "9e6742732c60:1",
  "hash": "ab91ba3994400a6d99c05a62981d3431df46aeb3640ffa5de6a132151313a6ec",
  "cid": "QmV1ab91ba3994400a6d99c05a62981d3431df46aeb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286392,
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
      "evaluated_at": 1760286392
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
  "sig": "e4d93ea4a15103350f7410d980943122b38102ec34c1bb83a8a916dace969f55"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000030232602
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}re': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7365830}}}