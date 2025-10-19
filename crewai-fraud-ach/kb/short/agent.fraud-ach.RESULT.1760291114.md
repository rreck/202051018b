```json
{
  "id": "a1043c5cb71234b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291114,
  "host_pid": "9e6742732c60:1",
  "hash": "86574eff850c2dd038a86193ad44887aab8fe122f4628ce085be395f577addc7",
  "cid": "QmV186574eff850c2dd038a86193ad44887aab8fe122",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291114,
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
      "evaluated_at": 1760291114
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
  "sig": "dad03ba9ec2ea1e9f17db26b08ef839996fbebbf60b74f1cc4853ea31f62d4a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 68709812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}