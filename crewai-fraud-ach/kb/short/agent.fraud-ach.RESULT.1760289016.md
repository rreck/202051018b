```json
{
  "id": "023bdb7da8634d35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289016,
  "host_pid": "9e6742732c60:1",
  "hash": "a6e92240dbf633e358f83bb02282935fed4aa41c4d4d9d232e84258ed94cf393",
  "cid": "QmV1a6e92240dbf633e358f83bb02282935fed4aa41c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289016,
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
      "evaluated_at": 1760289016
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
  "sig": "ce6fb96567fac85c27be5931a058a2da7ff5d4b4e8723e4538a4ead2cfbc58b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273476886
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 34054245, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': 'e52038f69d26fe5a'}}}aly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7209366}}}