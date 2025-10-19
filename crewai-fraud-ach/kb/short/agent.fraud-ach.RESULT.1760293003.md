```json
{
  "id": "c9fbdf136e9b5c23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293003,
  "host_pid": "9e6742732c60:1",
  "hash": "040b6a7907fce6628735ef5455e9121991ceee90627e368f27ff09cdcdc654b4",
  "cid": "QmV1040b6a7907fce6628735ef5455e9121991ceee90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293003,
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
      "evaluated_at": 1760293003
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
  "sig": "bfca63e92d8bf05dea557a074d8ef17a153bbb4487c364526b13d8b3b8d70e5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022135017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 15584503, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': 'ca41710ea386559e'}}}