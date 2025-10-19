```json
{
  "id": "ff020cfc4471353c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292132,
  "host_pid": "9e6742732c60:1",
  "hash": "7c6e28d0855d8ef2202549a846987958416f8f3794e6d1cdb6c96d081c324fdd",
  "cid": "QmV17c6e28d0855d8ef2202549a846987958416f8f37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292132,
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
      "evaluated_at": 1760292132
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
  "sig": "b910f5a230a49cd3349ec410e3ecfd55c7ec9baf79242f7cb9329f5662212c40"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029133644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 92924174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'fa9b9676ccddb30b'}}}