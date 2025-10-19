```json
{
  "id": "563a62778c98253e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294246,
  "host_pid": "9e6742732c60:1",
  "hash": "227aa8f3e93bc8036b6d9c86da11f9bee722ff0d77f896613bdecbf735507539",
  "cid": "QmV1227aa8f3e93bc8036b6d9c86da11f9bee722ff0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294246,
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
      "evaluated_at": 1760294246
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
  "sig": "b8c23d8e3f8971c96eb579f97b43c471db632f09594800cf50315e93233e6f7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 54287766, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}