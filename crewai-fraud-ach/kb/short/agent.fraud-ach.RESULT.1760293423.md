```json
{
  "id": "e188eb7b125c925a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293423,
  "host_pid": "9e6742732c60:1",
  "hash": "5b81bb9bd39d496ba3a934f09df3c975945c3b9acb4fb5c1532308d3cdfbdadc",
  "cid": "QmV15b81bb9bd39d496ba3a934f09df3c975945c3b9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293423,
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
      "evaluated_at": 1760293423
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
  "sig": "21e77b545505746eb678b40eaa3c565f496cd353fb7affbc156539987cbdf1cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592568865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 52752076, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}