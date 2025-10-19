```json
{
  "id": "5ba03c20843588ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289219,
  "host_pid": "9e6742732c60:1",
  "hash": "c1d32b921e5f6a4c6947c208c58629d29c869baec360a9fd4eea85d6f0833850",
  "cid": "QmV1c1d32b921e5f6a4c6947c208c58629d29c869bae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289219,
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
      "evaluated_at": 1760289219
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
  "sig": "117db9b9f2f2fa26e2b0c7901a890c102bcc42111ed5d33d1068bd4b5b98082c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596892918
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 29386656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'c247331c92498799'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}