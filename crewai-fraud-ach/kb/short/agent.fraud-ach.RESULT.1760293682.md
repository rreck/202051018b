```json
{
  "id": "89e6ba14800f2ced",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293682,
  "host_pid": "9e6742732c60:1",
  "hash": "52afce5499dfa78eb50a69de742eaabb1625b9392dd9c295efdea4818d367112",
  "cid": "QmV152afce5499dfa78eb50a69de742eaabb1625b939",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293682,
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
      "evaluated_at": 1760293682
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
  "sig": "728d8467ae85ee56452e5c5af42d2d41e514e3c807b661389ef597f85dce8443"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 90429399, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}