```json
{
  "id": "ef740a152142daaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293884,
  "host_pid": "9e6742732c60:1",
  "hash": "05b6252467d88b832504c2da2cc5c31c4c3729047e7e15d29417273c13fbecdd",
  "cid": "QmV105b6252467d88b832504c2da2cc5c31c4c372904",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293884,
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
      "evaluated_at": 1760293884
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
  "sig": "1946cea4c74e76d5be60ccf51092e7af3866fc3a346fa6fbb5c4b1d17b461000"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153371756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 94779310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': 'f6b71775dc53ea2e'}}}