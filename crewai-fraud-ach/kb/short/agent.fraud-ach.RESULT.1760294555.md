```json
{
  "id": "2384745c78ca469d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294555,
  "host_pid": "9e6742732c60:1",
  "hash": "495958ad0e69f490f275c7849f8fb308b612fcd8a6373e7f9a86ec25d5db4a81",
  "cid": "QmV1495958ad0e69f490f275c7849f8fb308b612fcd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294555,
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
      "evaluated_at": 1760294555
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
  "sig": "b1ee255ba16c84d7464ef5c1d92c17baa8effe6d53c9d68b03d012d389f29b71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021721554
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 43295040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '5c8161425a5b941f'}}}