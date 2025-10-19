```json
{
  "id": "51b7318e5e43a5ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294143,
  "host_pid": "9e6742732c60:1",
  "hash": "9814c36b8777f7fa1af2958e9ef9cba85f8a0db01d4f0dbc5b2c9a55265fc278",
  "cid": "QmV19814c36b8777f7fa1af2958e9ef9cba85f8a0db0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294143,
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
      "evaluated_at": 1760294143
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
  "sig": "fef79a8a97d9194ec9e41f905c0d8167093657a086d9059802600a18a6b2b64b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159548599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 23200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': '3450667ce2814f1a'}}}