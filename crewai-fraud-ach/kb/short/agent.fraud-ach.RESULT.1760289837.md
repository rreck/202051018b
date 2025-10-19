```json
{
  "id": "a8e6b54bf49b1674",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289837,
  "host_pid": "9e6742732c60:1",
  "hash": "4f0a3d828984836b49d0867fbc722045768cad4094d4896cc85b8fac387d6d93",
  "cid": "QmV14f0a3d828984836b49d0867fbc722045768cad40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289837,
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
      "evaluated_at": 1760289837
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
  "sig": "51f7c7516ba1e40d4d18eae73478bc115e2a11b95f06ced9de16e8c0d213de39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273461392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 47796728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': 'ee78248c8d3d65fe'}}}