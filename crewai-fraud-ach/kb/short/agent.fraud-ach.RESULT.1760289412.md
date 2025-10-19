```json
{
  "id": "bf1e143e0215792a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289412,
  "host_pid": "9e6742732c60:1",
  "hash": "99b58568725a255aff89c88939f1241928a858b0c29390c463fd574e1ef0a2d5",
  "cid": "QmV199b58568725a255aff89c88939f1241928a858b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289412,
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
      "evaluated_at": 1760289412
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
  "sig": "b59874acb05f9d62aa6e6be76dff5b0e58eda2de6fe118d2ec5b4491407aaee6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 50607552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}