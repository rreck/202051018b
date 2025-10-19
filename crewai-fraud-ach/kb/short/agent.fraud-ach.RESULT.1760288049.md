```json
{
  "id": "7798a595a289494f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288049,
  "host_pid": "9e6742732c60:1",
  "hash": "6a2b6b6bbbc0c4d55a51370faf9f10d25342fccc9fc2920a949e21ebd574ed4e",
  "cid": "QmV16a2b6b6bbbc0c4d55a51370faf9f10d25342fccc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288049,
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
      "evaluated_at": 1760288049
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
  "sig": "3fada9dae88b0519390db2650e4797f59883b4502c85764ce79992654e6e1f98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591397699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 11707902, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285764, 'matching_hash': '338c84efe55c1d97'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}