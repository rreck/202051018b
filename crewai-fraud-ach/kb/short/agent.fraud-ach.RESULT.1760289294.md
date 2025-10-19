```json
{
  "id": "395de1025d726206",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289294,
  "host_pid": "9e6742732c60:1",
  "hash": "339de369f8af5ba697f57097affd6d1332f5a142c0097c320d4fbe5a1e63d215",
  "cid": "QmV1339de369f8af5ba697f57097affd6d1332f5a142",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289294,
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
      "evaluated_at": 1760289294
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
  "sig": "58f4420fc1020389cdb653f720bd7863e9870dc3c85ea6b42bc28fc6fff8a9f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 16448418, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}