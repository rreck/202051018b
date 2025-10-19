```json
{
  "id": "7514be8a2f3f97e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289781,
  "host_pid": "9e6742732c60:1",
  "hash": "99803bf79b80e3380c5893d3e9c102121e962b5b984210646ac367ac9ab6748b",
  "cid": "QmV199803bf79b80e3380c5893d3e9c102121e962b5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289781,
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
      "evaluated_at": 1760289781
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
  "sig": "4bb4f1e6605e1f70ec12c8102aad0c55dfd08c18880d69a205dc8229e2bf3c4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}5763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018549}}}