```json
{
  "id": "fa2c2cfbaee7b776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289542,
  "host_pid": "9e6742732c60:1",
  "hash": "4a3c10da4b85aeeb44552aeb1f9a77aa8ae7386adaf850dea3a5766c39623c7b",
  "cid": "QmV14a3c10da4b85aeeb44552aeb1f9a77aa8ae7386a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289542,
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
      "evaluated_at": 1760289542
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
  "sig": "f274be635b0b6de8970f6998b652d1913b0b2d75100794aca8464fecee4cf30e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 51913764, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}