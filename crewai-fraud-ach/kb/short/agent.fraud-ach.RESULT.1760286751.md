```json
{
  "id": "f172559ada555f1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286751,
  "host_pid": "9e6742732c60:1",
  "hash": "adf4b475f3abb2750a70e041b520206ab122c4021330895591abc90414b2fdde",
  "cid": "QmV1adf4b475f3abb2750a70e041b520206ab122c402",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286751,
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
      "evaluated_at": 1760286751
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
  "sig": "35cfff977e2a8d1ce9f5db2ee4d869b8083612147039e2d7b99faa87bb6038f4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201466146132
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14285916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '20fb82cc575104fa'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}