```json
{
  "id": "4a528d47a65c5deb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290542,
  "host_pid": "9e6742732c60:1",
  "hash": "681aa1f5ca57b0c288bfd775c6d5888049fdd92d7ff2d5df1c0f36dee7b9fb4a",
  "cid": "QmV1681aa1f5ca57b0c288bfd775c6d5888049fdd92d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290542,
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
      "evaluated_at": 1760290542
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
  "sig": "600f3366604458a2daf8ecd2a89c9e9121acdcbcebb867c43a82848784b0fac3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 52455897, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}