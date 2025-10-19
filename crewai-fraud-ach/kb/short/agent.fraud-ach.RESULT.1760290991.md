```json
{
  "id": "3f3d6811fdfe658a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290991,
  "host_pid": "9e6742732c60:1",
  "hash": "d7b8e09b10a96cd12ba4cecb3d3bf89b0b11f39018258e4a6e84a10d3bf5d164",
  "cid": "QmV1d7b8e09b10a96cd12ba4cecb3d3bf89b0b11f390",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290991,
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
      "evaluated_at": 1760290991
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
  "sig": "fe6ecf1a5689e7279cddecf06059b84ad58ca45e5ae6fdf325bdd772790260f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158176118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 64492180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '15ef7d28467628fb'}}}