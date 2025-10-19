```json
{
  "id": "ddcf47f40295b2a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289969,
  "host_pid": "9e6742732c60:1",
  "hash": "7c403de544d559547e082bb0117cedfad552f6fec003704e3fc02574e008c68b",
  "cid": "QmV17c403de544d559547e082bb0117cedfad552f6fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289969,
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
      "evaluated_at": 1760289969
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
  "sig": "76c976430b0a6f2d0a68945d8198e94c68e29353bef64a5128f11e915734bc37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026865262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 67584258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'acc989ae5f5d7052'}}}aly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}