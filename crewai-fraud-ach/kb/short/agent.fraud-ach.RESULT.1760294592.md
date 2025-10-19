```json
{
  "id": "b90c1202f7d74883",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294592,
  "host_pid": "9e6742732c60:1",
  "hash": "d57a861ce74f409380f335da2695b4f1e06bf9920a0953a3750fa813abb6620a",
  "cid": "QmV1d57a861ce74f409380f335da2695b4f1e06bf992",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294592,
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
      "evaluated_at": 1760294592
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
  "sig": "737774f2ba6282358eb8da43033e99caab70f18a571d0addeeae57dd5341887e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022691878
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 12741911, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'a2c26d052e86193d'}}}