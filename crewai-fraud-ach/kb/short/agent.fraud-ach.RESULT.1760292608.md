```json
{
  "id": "0999ed23a6066c33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292608,
  "host_pid": "9e6742732c60:1",
  "hash": "3337135cb4abd2f12ee1f773e6d08e2de956fe986a60833053c49be9256d08bd",
  "cid": "QmV13337135cb4abd2f12ee1f773e6d08e2de956fe98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292608,
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
      "evaluated_at": 1760292608
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
  "sig": "d84fc12128fbc2f34be4a286a1df26ba1e83bb60222e44f4ddac510978fc7ee5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022029056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 39537504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '0de74255bde38153'}}}}