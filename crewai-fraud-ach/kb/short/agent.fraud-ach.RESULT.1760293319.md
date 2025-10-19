```json
{
  "id": "9eac18689361a64a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293319,
  "host_pid": "9e6742732c60:1",
  "hash": "817586ad721916d81717532b798515e04c0f7165884147d336ad9763eff7203a",
  "cid": "QmV1817586ad721916d81717532b798515e04c0f7165",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293319,
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
      "evaluated_at": 1760293319
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
  "sig": "c0f801a4bb8d9399bf34ac6ef3be3d308247129d5f28f10ecf7975daebdd59f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150046055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 84905064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': 'b44312efb353b904'}}}