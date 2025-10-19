```json
{
  "id": "1892347340351207",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289980,
  "host_pid": "9e6742732c60:1",
  "hash": "86f40e9002c1f0cc5b82f7d1d8c859e49807be64ceee9c37bf5a90f7c5f9d3fe",
  "cid": "QmV186f40e9002c1f0cc5b82f7d1d8c859e49807be64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289980,
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
      "evaluated_at": 1760289980
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
  "sig": "dd420248db0283bacf2f152b0464c550f1e02aca3f17ccdaffb0bcc378ef49ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 34755714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}