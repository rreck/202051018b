```json
{
  "id": "2556362ac1e06ffa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293311,
  "host_pid": "9e6742732c60:1",
  "hash": "f42d37ed33fd2357d015b48eb97de3e263e6ba99b6f08e2df7f9a0ff91b601cc",
  "cid": "QmV1f42d37ed33fd2357d015b48eb97de3e263e6ba99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293311,
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
      "evaluated_at": 1760293311
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
  "sig": "a8606ae64e28f7173a736e39f166a564541a5dfd745173f2466f31da62d03067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 35488800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}