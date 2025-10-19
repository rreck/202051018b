```json
{
  "id": "c8d0720650a8be34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292636,
  "host_pid": "9e6742732c60:1",
  "hash": "cfffc85f49526ef644801dc2ac51b4ba05fda9b153f3f8034d4e502f2d30e5b6",
  "cid": "QmV1cfffc85f49526ef644801dc2ac51b4ba05fda9b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292636,
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
      "evaluated_at": 1760292636
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
  "sig": "a773a5cb5340bf8763052c1caa887d0cf4d3bfd0a1b413214331ae6763b64f74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591751649
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 57712612, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'aa8323f9af9da717'}}}