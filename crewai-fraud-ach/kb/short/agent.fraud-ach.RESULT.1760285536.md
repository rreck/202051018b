```json
{
  "id": "0430135e89c6fe16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285536,
  "host_pid": "9e6742732c60:1",
  "hash": "5445bdf171aed7c415e024f9a39178c730d5ba48884ae3380deb1c975e3d8223",
  "cid": "QmV15445bdf171aed7c415e024f9a39178c730d5ba48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285536,
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
      "evaluated_at": 1760285536
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
  "sig": "97628b3d69f7b8369683bc3107c2a5c73dbd43520df1a435b4eaaa00f307d8b1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 23176670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}