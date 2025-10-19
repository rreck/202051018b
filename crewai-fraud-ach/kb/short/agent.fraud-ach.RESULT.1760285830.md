```json
{
  "id": "8517644d19972c6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285830,
  "host_pid": "9e6742732c60:1",
  "hash": "92ff285c5784feee26d829767430879f1a8c33c8cdc891144102135634a9a069",
  "cid": "QmV192ff285c5784feee26d829767430879f1a8c33c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285830,
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
      "evaluated_at": 1760285830
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
  "sig": "96f8b6b1f1e7037c01209dd8971f9a665828ee072ed78ebf66cec6abad271a25"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}