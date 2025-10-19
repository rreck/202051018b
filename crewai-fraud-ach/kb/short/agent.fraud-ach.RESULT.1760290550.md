```json
{
  "id": "9147357fcea74942",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290550,
  "host_pid": "9e6742732c60:1",
  "hash": "3e057ef5dc16e1c01bcfd1d0ade1c63d44e8c48f6ea1423dc3bed0610b9b8a7b",
  "cid": "QmV13e057ef5dc16e1c01bcfd1d0ade1c63d44e8c48f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290550,
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
      "evaluated_at": 1760290550
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
  "sig": "0300760269ca13b2d1837f3b768cd3919c809920c5aec4d0c30c51460e2a1c5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 73129776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}