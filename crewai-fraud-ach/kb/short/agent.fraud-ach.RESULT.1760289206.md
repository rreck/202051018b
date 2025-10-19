```json
{
  "id": "66d0eba3b3711e89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289206,
  "host_pid": "9e6742732c60:1",
  "hash": "8ab8b0a9291ea793f30032530d733f5460e34906455f1fdc465ef4f63eaae61a",
  "cid": "QmV18ab8b0a9291ea793f30032530d733f5460e34906",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289206,
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
      "evaluated_at": 1760289206
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
  "sig": "c260b56ff3d380d9e8783562ad297ecb3001896f5e334eb41b5cdd4cfd601461"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 36916768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}