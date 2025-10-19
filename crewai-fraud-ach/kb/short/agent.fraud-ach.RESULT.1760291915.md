```json
{
  "id": "a5de9c2575e7233a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291915,
  "host_pid": "9e6742732c60:1",
  "hash": "55951794a73f7009a74f3302ad36932e79a2e9a5dbc9e740a14738342c65d48b",
  "cid": "QmV155951794a73f7009a74f3302ad36932e79a2e9a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291915,
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
      "evaluated_at": 1760291915
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
  "sig": "f525fd0b01c94daa69783f78478071dab0c21b22d509acd1dc79479cd8cee220"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 16323360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}