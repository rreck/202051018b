```json
{
  "id": "3609deccd067c33e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294918,
  "host_pid": "9e6742732c60:1",
  "hash": "0f2191750f47c55614e5689e9389b06abd98a786265f33860b091408df070b82",
  "cid": "QmV10f2191750f47c55614e5689e9389b06abd98a786",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294918,
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
      "evaluated_at": 1760294918
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
  "sig": "0a625ab5e12a2ce8f87806bfd239a2e237f60ce772f74a301fa7ce431ca40c6b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362528
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 105586325, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '85f76e3ae9d0eff6'}}}