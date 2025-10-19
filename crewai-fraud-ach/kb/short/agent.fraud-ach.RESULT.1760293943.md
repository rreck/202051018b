```json
{
  "id": "28eb7c17d6af559d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293943,
  "host_pid": "9e6742732c60:1",
  "hash": "3dfdaacc150ff035d5ba4d28d640332c39088c991436de24b6647b54a7091164",
  "cid": "QmV13dfdaacc150ff035d5ba4d28d640332c39088c99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293943,
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
      "evaluated_at": 1760293943
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
  "sig": "fa3329a9383533cc0b2c5de5e8e681cf2b5d5a4a1be76d4c246a49aa24f50c86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 26037144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}