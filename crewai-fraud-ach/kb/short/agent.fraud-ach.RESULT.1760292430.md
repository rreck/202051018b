```json
{
  "id": "6b568d089940b84f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292430,
  "host_pid": "9e6742732c60:1",
  "hash": "f0ff915c5120446e8498cd051d15e2a19b21592e1d6c35044ff070ce1ea95dc7",
  "cid": "QmV1f0ff915c5120446e8498cd051d15e2a19b21592e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292430,
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
      "evaluated_at": 1760292430
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
  "sig": "9abbaba5615b1b60cee17c2847a6d36a694ee7b9605a984c639f8c7d86b60ae1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 72352190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}