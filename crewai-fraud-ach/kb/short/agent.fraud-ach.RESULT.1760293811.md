```json
{
  "id": "2c67ea57f6590eba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293811,
  "host_pid": "9e6742732c60:1",
  "hash": "ccad0de1f9f1f301bcc2753090e680fe0d6b1a4cf61e96ec97284c270a4dfc60",
  "cid": "QmV1ccad0de1f9f1f301bcc2753090e680fe0d6b1a4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293811,
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
      "evaluated_at": 1760293811
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
  "sig": "039b9bf10504d69257a4e8c3befcee8c5a437f1addc6ea53076cca5beec759c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596354415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 62903710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'f20df65cb297838c'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9245331}}}