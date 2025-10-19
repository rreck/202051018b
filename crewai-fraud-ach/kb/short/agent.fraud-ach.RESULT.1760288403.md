```json
{
  "id": "890a3d269af8d8f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288403,
  "host_pid": "9e6742732c60:1",
  "hash": "a8bb5e44ec8c18e3b0606ad5291fad38379edbf9f236a3367fdb3a82d590ef4d",
  "cid": "QmV1a8bb5e44ec8c18e3b0606ad5291fad38379edbf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288403,
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
      "evaluated_at": 1760288403
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
  "sig": "ca74b0c3aee20c1220259b8b302d6a5e532466374ef955ad23bc9991af713eac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 37045088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}