```json
{
  "id": "b72a7adecb09d6b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289501,
  "host_pid": "9e6742732c60:1",
  "hash": "30fd1d20f23b2f9b033b7b74f92d43b13938ea5de5e90cb3cf319e8dd7e279d7",
  "cid": "QmV130fd1d20f23b2f9b033b7b74f92d43b13938ea5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289501,
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
      "evaluated_at": 1760289501
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
  "sig": "41a38cae79c311d4913c59920ade02af3c3d65e9d7d2cfdd02febb26be8226ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592248809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 21685500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'ed3ae9155c1e3edb'}}}