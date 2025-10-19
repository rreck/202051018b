```json
{
  "id": "1ac9845936de090b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287788,
  "host_pid": "9e6742732c60:1",
  "hash": "6ce29dc0b06e4cbdb38daa80222fa3e585cac4f616ce97cc8ecbc40850cc0bcc",
  "cid": "QmV16ce29dc0b06e4cbdb38daa80222fa3e585cac4f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287788,
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
      "evaluated_at": 1760287788
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
  "sig": "3ffea9324374cacea7770a902744c0b7ea24f7bb0588422fc1a5501fd0017988"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 32319936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}