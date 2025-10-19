```json
{
  "id": "d9cb7d1781caf511",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289756,
  "host_pid": "9e6742732c60:1",
  "hash": "660b1bfbd3e7e9428f41852b9b3c8d769bc02bba1ced7c07ea122c3b5d5ef5e2",
  "cid": "QmV1660b1bfbd3e7e9428f41852b9b3c8d769bc02bba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289756,
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
      "evaluated_at": 1760289756
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
  "sig": "56793ccdc60eac8d115b86f0da6a8ff53b87526b161a8ba954cea92e96053395"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591685004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 43409784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}