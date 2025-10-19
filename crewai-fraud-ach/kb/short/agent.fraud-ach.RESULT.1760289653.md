```json
{
  "id": "de74803363e960ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289653,
  "host_pid": "9e6742732c60:1",
  "hash": "053c88c0ca95803fccd095cc15ec6105fcf7a7710a759728c13280e7ebdd10f1",
  "cid": "QmV1053c88c0ca95803fccd095cc15ec6105fcf7a771",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289653,
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
      "evaluated_at": 1760289653
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
  "sig": "44b9ed85a7b6e9be4d83df4534bace09e90a20c1123853a2b80a80397e82abec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 29927871, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}