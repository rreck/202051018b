```json
{
  "id": "5b7670b9ec3e39bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292117,
  "host_pid": "9e6742732c60:1",
  "hash": "bdf4bd8497b3f08813e7279aa185cae064f79db3fb84ba07170689d2dd93dc68",
  "cid": "QmV1bdf4bd8497b3f08813e7279aa185cae064f79db3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292117,
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
      "evaluated_at": 1760292117
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
  "sig": "172f7679af33d7a85d88ddbdbbea38f3e1185937c47ba2c50aac29c27f3920c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 60467120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}