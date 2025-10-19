```json
{
  "id": "ac5ae3f9b870645e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286184,
  "host_pid": "9e6742732c60:1",
  "hash": "263b3a4275bca201998ad64724f8547896c1f9988c3db32aa5be0315cd1ab976",
  "cid": "QmV1263b3a4275bca201998ad64724f8547896c1f998",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286184,
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
      "evaluated_at": 1760286184
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
  "sig": "805e1f14377a366baf79fd725ce77bff61155e18b11765cdaa0e9ed9bc6c1a93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466150314
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 26174664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760284979, 'matching_hash': '93cc3488fa8b8da9'}}}