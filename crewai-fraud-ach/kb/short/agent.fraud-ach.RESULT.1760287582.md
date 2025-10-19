```json
{
  "id": "eb918289e262df8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287582,
  "host_pid": "9e6742732c60:1",
  "hash": "60fab9416ee523f3717e0393a05ea8b571ce137ff2a6b81e13118a99d479db54",
  "cid": "QmV160fab9416ee523f3717e0393a05ea8b571ce137f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287582,
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
      "evaluated_at": 1760287582
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
  "sig": "84d1615b2a233d58b2807a8f45df25341be5c2ac0cf4292933b274ab24293738"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 29378440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}