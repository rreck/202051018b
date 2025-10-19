```json
{
  "id": "be295cf8881554ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291198,
  "host_pid": "9e6742732c60:1",
  "hash": "5146a1edd1801d3814ce6c0c2be32236e6c7610ddbbb1f1229e69e3f7d31c75a",
  "cid": "QmV15146a1edd1801d3814ce6c0c2be32236e6c7610d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291198,
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
      "evaluated_at": 1760291198
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
  "sig": "66b6cd1813b732b61b2c48060dd69add1a390df5a7c90ae45f93d25304802a84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279970164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 31206188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}