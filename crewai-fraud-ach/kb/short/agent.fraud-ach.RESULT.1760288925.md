```json
{
  "id": "9cdf68d93d4bb72f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288925,
  "host_pid": "9e6742732c60:1",
  "hash": "b0d458cd28131321a9c57faedb93ba868f193bf358ad166943b1c8f04ec9795e",
  "cid": "QmV1b0d458cd28131321a9c57faedb93ba868f193bf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288925,
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
      "evaluated_at": 1760288925
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
  "sig": "d60b9687635936ceb89afb0cd1d57211d2debb19a3d77c92c3fb5fe759c68293"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026697062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 58747152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}