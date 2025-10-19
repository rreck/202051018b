```json
{
  "id": "c90b1fd2d64308ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293150,
  "host_pid": "9e6742732c60:1",
  "hash": "4e8274e0e2ca50591bd85031d3acbeb3ab7064a3f7f2c008ab3417970b55449b",
  "cid": "QmV14e8274e0e2ca50591bd85031d3acbeb3ab7064a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293150,
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
      "evaluated_at": 1760293150
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
  "sig": "b2efe9d6f17a0c82a8c0a57c622bb592a71f59904c5c737a169dc0811dc1b2c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 67468576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}