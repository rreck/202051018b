```json
{
  "id": "7f16f12e3c53cbe9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289725,
  "host_pid": "9e6742732c60:1",
  "hash": "ceb677eb44265ebc47bc33ce0ee3a144795453ae868bd1c1d391384fef7ed91a",
  "cid": "QmV1ceb677eb44265ebc47bc33ce0ee3a144795453ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289725,
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
      "evaluated_at": 1760289725
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
  "sig": "35894a2623a8c6bacea07a4e5c7cac82f8e08387ffe4cb7040a9247e191eb132"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 21486751, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}