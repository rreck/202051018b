```json
{
  "id": "1c25361d82528dbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293275,
  "host_pid": "9e6742732c60:1",
  "hash": "67f77813f62c377d5e93202fd26e6d85d4cff5d7eac0347a0b7315519246839d",
  "cid": "QmV167f77813f62c377d5e93202fd26e6d85d4cff5d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293275,
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
      "evaluated_at": 1760293275
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
  "sig": "3474a8b314102f2255b51405612fab20520719b40607bb2033560e300a84372c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592473066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 70328865, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '48f07b8f6bc31034'}}}