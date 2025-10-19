```json
{
  "id": "3fa900aa25728944",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290463,
  "host_pid": "9e6742732c60:1",
  "hash": "fe293c4f9a5315fa2399b4c18f4b9f8623657e2e5b2b9a3cc5582a4240d139e7",
  "cid": "QmV1fe293c4f9a5315fa2399b4c18f4b9f8623657e2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290463,
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
      "evaluated_at": 1760290463
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
  "sig": "429e56f1b2433ca4ba69e4aafa3ce834e7fd2707f6a40d2a9e58380b1302cae1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 66475183, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}