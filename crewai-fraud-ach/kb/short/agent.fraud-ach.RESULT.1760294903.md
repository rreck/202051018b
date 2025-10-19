```json
{
  "id": "2dd062443b476cf6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294903,
  "host_pid": "9e6742732c60:1",
  "hash": "b7edcc4b87600beebdb91591d860edd08a9df6ffc560cc6a3e50996aa1b0fbeb",
  "cid": "QmV1b7edcc4b87600beebdb91591d860edd08a9df6ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294903,
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
      "evaluated_at": 1760294903
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
  "sig": "1bffb59ed9c58328c46a0db753303c6c672cb691ce4e9fc65201e4f13a7374d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 78289008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}