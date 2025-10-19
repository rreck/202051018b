```json
{
  "id": "6850b52ead95a47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294029,
  "host_pid": "9e6742732c60:1",
  "hash": "8069764639e6e29f23405412108ddfc329ff8d33bb31b71a9fe52690587457d8",
  "cid": "QmV18069764639e6e29f23405412108ddfc329ff8d33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294029,
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
      "evaluated_at": 1760294029
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
  "sig": "1ef61b8fd1fa63d023a086dc14142d7fec3683663089d7316e23badffa34a7e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 71807840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}