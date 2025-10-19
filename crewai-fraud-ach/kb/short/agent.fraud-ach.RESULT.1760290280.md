```json
{
  "id": "49ed0b83f17d461d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290280,
  "host_pid": "9e6742732c60:1",
  "hash": "b5daa6632362bd3642185a61887fa7ea75f90622f105270dc6a681063a820357",
  "cid": "QmV1b5daa6632362bd3642185a61887fa7ea75f90622",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290280,
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
      "evaluated_at": 1760290280
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
  "sig": "767be1fa336862b44b8f691db3e748ee6724e4d79f43197589da1577cb2cf280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031032710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 34631346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'e5dc8a38744b9e1c'}}}