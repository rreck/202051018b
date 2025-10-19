```json
{
  "id": "8c9d3bb380308c3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288684,
  "host_pid": "9e6742732c60:1",
  "hash": "1e0598e07104ac16d7995b50a11760e0ed13697de20232e8b844d8cf8f8d028d",
  "cid": "QmV11e0598e07104ac16d7995b50a11760e0ed13697d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288684,
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
      "evaluated_at": 1760288684
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
  "sig": "df369ed1e8123306846692489edf471d2d615096e93cdff6f945152ff4be1421"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591082294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 46910561, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': 'b890dc886075e9be'}}}aly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.08, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9655961}}}