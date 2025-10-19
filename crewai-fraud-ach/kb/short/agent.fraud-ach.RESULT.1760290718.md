```json
{
  "id": "3b2deba481f9f5dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290718,
  "host_pid": "9e6742732c60:1",
  "hash": "30a9505e25cf803047dfe8b3ab1248c98884173d02767bab78be28efa63f7bb4",
  "cid": "QmV130a9505e25cf803047dfe8b3ab1248c98884173d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290718,
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
      "evaluated_at": 1760290718
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
  "sig": "120bbee90931acd8db8749f1426c3e69f56a8a2fec01f062bb1137beacf9f7b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594086126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 21324839, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': '58168677024efb84'}}}