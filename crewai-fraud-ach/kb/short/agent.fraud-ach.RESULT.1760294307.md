```json
{
  "id": "2e7b0c165a3367d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294307,
  "host_pid": "9e6742732c60:1",
  "hash": "68f96b3514a587db57c4baeff6b28a15523de5b010fee7aaba9bc32d8514576e",
  "cid": "QmV168f96b3514a587db57c4baeff6b28a15523de5b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294307,
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
      "evaluated_at": 1760294307
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
  "sig": "2a943fbb7bb9d59620966c1ea8f74e5e8988e9d51fab30cdc288aa4c5a0f59c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275925775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 45534305, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': 'faef3b4bfd0d33cd'}}}