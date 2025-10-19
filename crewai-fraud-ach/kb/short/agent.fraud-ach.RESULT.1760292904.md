```json
{
  "id": "efaee5b34ff41a3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292904,
  "host_pid": "9e6742732c60:1",
  "hash": "93d2c7ca12197fe98df5a64831f21af625a7cbfa410c62afd95c214a033a2f97",
  "cid": "QmV193d2c7ca12197fe98df5a64831f21af625a7cbfa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292904,
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
      "evaluated_at": 1760292904
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
  "sig": "0dc3757c2e838fea9730af54fbe6ef0381de35dc00d1fc91b59e09f9033da09d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 41394204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}