```json
{
  "id": "8be6124893d2d975",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293841,
  "host_pid": "9e6742732c60:1",
  "hash": "2e17874753ed2845408e6f16d682de9d9987b8b3e90f8c9c8556695531b43c0f",
  "cid": "QmV12e17874753ed2845408e6f16d682de9d9987b8b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293841,
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
      "evaluated_at": 1760293841
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
  "sig": "0575f903b417954dd4c5a423ceb84d4b1d8d21b0becb9f7050d9663d4c5e1bd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 71924048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}