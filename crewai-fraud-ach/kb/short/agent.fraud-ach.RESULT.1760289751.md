```json
{
  "id": "f95a18d153c1c61f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289751,
  "host_pid": "9e6742732c60:1",
  "hash": "46dcdcbdbf50b2cd987e2f9c397c9d9a6f9a14b4e10e5f04d85d718899ae1d7e",
  "cid": "QmV146dcdcbdbf50b2cd987e2f9c397c9d9a6f9a14b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289751,
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
      "evaluated_at": 1760289751
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
  "sig": "bddc83e4885f4ed7521b7eda38156079819f321e4c964f0b025b210312efb19b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598799064
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 49667904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '14e8b5e643b0ea13'}}}