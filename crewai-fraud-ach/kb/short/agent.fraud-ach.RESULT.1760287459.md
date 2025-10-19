```json
{
  "id": "37b8dbdc04d5fa0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287459,
  "host_pid": "9e6742732c60:1",
  "hash": "0c286a0addab8dea4ed3e3015b4771771b97938f644ed8a9c21eb94292941db2",
  "cid": "QmV10c286a0addab8dea4ed3e3015b4771771b97938f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287459,
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
      "evaluated_at": 1760287459
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "227e3897cefeeaf75111bf8af8713c06301f45e896ce311f03c4133a9c5011aa"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 021000022696777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 29712002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': 'bb01014ea9b32f36'}}}