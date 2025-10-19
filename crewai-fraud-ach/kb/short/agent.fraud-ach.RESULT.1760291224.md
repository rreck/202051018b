```json
{
  "id": "66eba9d1297a6c63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291224,
  "host_pid": "9e6742732c60:1",
  "hash": "983203115db936b096fb70b4564ce19ccdec6ef7412a809fbb47cd737203d2d6",
  "cid": "QmV1983203115db936b096fb70b4564ce19ccdec6ef7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291224,
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
      "evaluated_at": 1760291224
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
  "sig": "45871d147a0237c684d9b2b52a2caea767786930da4fe88b673be54c62d52789"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 22699590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}