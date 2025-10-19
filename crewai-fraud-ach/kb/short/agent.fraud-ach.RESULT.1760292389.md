```json
{
  "id": "65049ecedff19b88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292389,
  "host_pid": "9e6742732c60:1",
  "hash": "32cb8e6ba35ed2c054deac588143c38ad996a8b281ac1e7efa03fb51db7feb83",
  "cid": "QmV132cb8e6ba35ed2c054deac588143c38ad996a8b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292389,
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
      "evaluated_at": 1760292389
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
  "sig": "82210d360c4b71fa49a8341fbe19268f9e15627cdd7794026365f6336fa33bfe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593122933
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 79305324, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': '1a44b34bf830cda9'}}}