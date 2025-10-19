```json
{
  "id": "07c6c6074aaf04e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292057,
  "host_pid": "9e6742732c60:1",
  "hash": "938dfcf2b23e549f130a2cffb8c5d9bb6aef553f603361e381735c72ba831731",
  "cid": "QmV1938dfcf2b23e549f130a2cffb8c5d9bb6aef553f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292057,
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
      "evaluated_at": 1760292057
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
  "sig": "3476bfe3924c7f714d41b4e2c34843f0deb38d3eab297a08748608f4597a374f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 265, 'threshold': 50, 'total_amount': 128572965, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 264, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}aly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6131353}}}