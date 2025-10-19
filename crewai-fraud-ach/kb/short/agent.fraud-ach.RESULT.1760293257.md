```json
{
  "id": "c77cec62ba68d1c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293257,
  "host_pid": "9e6742732c60:1",
  "hash": "5adc6ca979bdfe61a4875b6e3c7b9e5cbd07e616310e4440c65b559c5fadb22d",
  "cid": "QmV15adc6ca979bdfe61a4875b6e3c7b9e5cbd07e616",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293257,
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
      "evaluated_at": 1760293257
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
  "sig": "f12b3401480252d30e4dc41b688f36558de82dd309c6198412d68f42dbb4b9f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591034480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 87477695, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '8ba7f443842400ac'}}}