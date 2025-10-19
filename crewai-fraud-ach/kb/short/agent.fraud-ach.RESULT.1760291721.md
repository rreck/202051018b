```json
{
  "id": "464bd7032bcd9278",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291721,
  "host_pid": "9e6742732c60:1",
  "hash": "9593f50d2351e00ce599b92c9991401cf556d1ffaf8ada053e65c6dc9a651552",
  "cid": "QmV19593f50d2351e00ce599b92c9991401cf556d1ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291721,
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
      "evaluated_at": 1760291721
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
  "sig": "03163b25c2e17f16ba5a2589b23c3081c39fbd845af9aad9f77a066b0d60db5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 57602888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}