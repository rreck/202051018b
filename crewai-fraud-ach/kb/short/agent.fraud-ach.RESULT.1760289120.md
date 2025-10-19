```json
{
  "id": "419826243866af9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289120,
  "host_pid": "9e6742732c60:1",
  "hash": "6e1dced3d174760a7bff9d3318f0783b178699f17044cf924a3f5cdb7a498b97",
  "cid": "QmV16e1dced3d174760a7bff9d3318f0783b178699f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289120,
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
      "evaluated_at": 1760289120
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
  "sig": "103387ed29e3b2bba680b6468ac29029f1c0f96c8f8ffa7dc643102a1f1c72a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240263900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 28500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}