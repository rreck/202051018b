```json
{
  "id": "db6f4d805289c369",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289200,
  "host_pid": "9e6742732c60:1",
  "hash": "6b3b81658568abec05420637a2026f9dfbca6bd5aebf5229bdeffad39733a8b9",
  "cid": "QmV16b3b81658568abec05420637a2026f9dfbca6bd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289200,
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
      "evaluated_at": 1760289200
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
  "sig": "5b45b6d1c01913e0be50331665b4b06331c2349551ae87b802ef23398c00fba3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 11858796, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}