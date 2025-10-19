```json
{
  "id": "c0504d48359096c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294482,
  "host_pid": "9e6742732c60:1",
  "hash": "853365961b52c7225b891f733144cc5161d0d8d5708df82152bca2df5e3f09c3",
  "cid": "QmV1853365961b52c7225b891f733144cc5161d0d8d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294482,
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
      "evaluated_at": 1760294482
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
  "sig": "a5443ae56e422f9ad98ae06bf50d188ea9b3c475a63a1ef83ae325f0aae8bf84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 101571415, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}