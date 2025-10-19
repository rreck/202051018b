```json
{
  "id": "bfcb66c1b196c246",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294098,
  "host_pid": "9e6742732c60:1",
  "hash": "2350bbcc44b806985d711bbf53c51204f7cc729086730d69a204aa451317ebcc",
  "cid": "QmV12350bbcc44b806985d711bbf53c51204f7cc7290",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294098,
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
      "evaluated_at": 1760294098
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
  "sig": "a62c3d28b52d96263a7ffc347052f5ffcc6e819a675e6da5341e0f625595a685"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275925775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 44759253, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'faef3b4bfd0d33cd'}}}