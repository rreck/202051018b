```json
{
  "id": "be88614ab0c68996",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287100,
  "host_pid": "9e6742732c60:1",
  "hash": "f66cfafd2270099b93f7b24ab1eae82babeac0cc659acc0f992b69751f7d651c",
  "cid": "QmV1f66cfafd2270099b93f7b24ab1eae82babeac0cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287100,
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
      "evaluated_at": 1760287100
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4ae0840889a50a9acb4124f5d5e69287a2bba71069b3108a73c5a8544425c626"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105158176118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18875760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': '15ef7d28467628fb'}}}