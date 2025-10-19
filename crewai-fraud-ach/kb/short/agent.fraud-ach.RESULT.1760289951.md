```json
{
  "id": "a023a03cdf910b2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289951,
  "host_pid": "9e6742732c60:1",
  "hash": "300d29d604781ac847f9d5cdca56a7b21db5c652da7dd0fba7653ec46b6cd4a3",
  "cid": "QmV1300d29d604781ac847f9d5cdca56a7b21db5c652",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289951,
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
      "evaluated_at": 1760289951
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "658db8b365baee2a600836ed5a36e9ea2e810bdaf760ec88a18ba217d1329596"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000023602502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 137000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': 'eacad8d3d1630a37'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}