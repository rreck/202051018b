```json
{
  "id": "f4dd13f9cb8502ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287329,
  "host_pid": "9e6742732c60:1",
  "hash": "c5319cf79f1bc4fe9340240982774cbe9055310eeadf6144c8ad816f837a9b67",
  "cid": "QmV1c5319cf79f1bc4fe9340240982774cbe9055310e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287329,
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
      "evaluated_at": 1760287329
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "606a3ce8a079e61a0d68f6f958c9b639766de4b6ce059de68c954dbba7497b5f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 20260184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}