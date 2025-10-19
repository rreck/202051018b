```json
{
  "id": "d1454d8aef6c7cda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289148,
  "host_pid": "9e6742732c60:1",
  "hash": "0f88ffc433b88b0f2e80839af79fae66d41a58da4716a1603b9245b0a58ab6b4",
  "cid": "QmV10f88ffc433b88b0f2e80839af79fae66d41a58da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289148,
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
      "evaluated_at": 1760289148
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
  "sig": "0122bbff4af1876b52cfab06a1d3258c40c6f51bf89268d4348a7518196ac412"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158127705
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 33779295, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': 'c9228fea95a929fd'}}}