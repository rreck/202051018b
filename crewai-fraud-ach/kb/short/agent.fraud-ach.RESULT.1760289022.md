```json
{
  "id": "076ebb7994dc6c3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289022,
  "host_pid": "9e6742732c60:1",
  "hash": "c57de96cc46390b698e2575b3187283c490e22d907e1b1b916f6d7cfccc1f232",
  "cid": "QmV1c57de96cc46390b698e2575b3187283c490e22d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289022,
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
      "evaluated_at": 1760289022
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
  "sig": "c2ee43d80afec20e796deddc3df63287269cdfe8e0194053744b1ac07611423f"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 111000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}