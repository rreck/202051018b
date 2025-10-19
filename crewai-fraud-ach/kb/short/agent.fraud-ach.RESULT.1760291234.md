```json
{
  "id": "ac7487a99f20d73b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291234,
  "host_pid": "9e6742732c60:1",
  "hash": "a8fc24df9bfe271bbb701ba2babf904db75b85c3416e914e93458bcf7283f725",
  "cid": "QmV1a8fc24df9bfe271bbb701ba2babf904db75b85c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291234,
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
      "evaluated_at": 1760291234
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
  "sig": "c47fccaa7cac13643369754dea60ca4f6a279bab0bdd89ec1f2c8399bc18e4b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028786297
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 56630230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'f6cfe00d30182bd5'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}