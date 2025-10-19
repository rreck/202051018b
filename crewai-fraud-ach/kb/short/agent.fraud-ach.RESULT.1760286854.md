```json
{
  "id": "20035e5ca56fc7e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286854,
  "host_pid": "9e6742732c60:1",
  "hash": "01f0ab9106829138863aa9ebdaedc59df7fb850cf815b0dabdf48310e09c9b8f",
  "cid": "QmV101f0ab9106829138863aa9ebdaedc59df7fb850c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286854,
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
      "evaluated_at": 1760286854
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
  "sig": "16af026464444f3654d1451c9d1cc9524afb2681db5a83c9c74f4d304af2e5d9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12411672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}