```json
{
  "id": "ab416e25545c2a87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289227,
  "host_pid": "9e6742732c60:1",
  "hash": "6bb02ee7bfa4dcd43540564ca6697a699cb202fef4894ba006aecb2c9b08684d",
  "cid": "QmV16bb02ee7bfa4dcd43540564ca6697a699cb202fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289227,
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
      "evaluated_at": 1760289227
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
  "sig": "fd6d151869af87bd1cf85378013bc8c2a7ee1ad5b07e0d5bb9197cb92a673f2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277495051
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 56971161, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'b54d2b84a0558fd6'}}}