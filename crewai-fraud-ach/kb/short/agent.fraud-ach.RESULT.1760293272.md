```json
{
  "id": "ccf2d75f587af53a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293272,
  "host_pid": "9e6742732c60:1",
  "hash": "cdf8caeb37fa6eaf915cf4836bd10d516022c48795d9e00a5c3ebe0a5cd11c2f",
  "cid": "QmV1cdf8caeb37fa6eaf915cf4836bd10d516022c487",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293272,
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
      "evaluated_at": 1760293272
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
  "sig": "670c6adad7e0082a1b22c4392c0792c3f1e179493eac3a1beceb7a20e6a63c0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 44292580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}