```json
{
  "id": "100e447b41d79e72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292547,
  "host_pid": "9e6742732c60:1",
  "hash": "3887aa0e238ad076f4e7772375b6151fce3e2679e7b3765c75aa043d7347358a",
  "cid": "QmV13887aa0e238ad076f4e7772375b6151fce3e2679",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292547,
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
      "evaluated_at": 1760292547
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
  "sig": "d23f93f3d4821036cb533c9d30f6fb483464c3619b771511859ad513aabbaf93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150980279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 44968000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '8a0222b527408f48'}}}