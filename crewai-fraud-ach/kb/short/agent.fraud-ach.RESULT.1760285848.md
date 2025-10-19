```json
{
  "id": "213611adc868074f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285848,
  "host_pid": "9e6742732c60:1",
  "hash": "29f9db5052075cc8770307274ca9779a80aad352f4195804745440bc4bd24184",
  "cid": "QmV129f9db5052075cc8770307274ca9779a80aad352",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285848,
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
      "evaluated_at": 1760285848
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
  "sig": "12e6b451a2f519ef3ed05b306ee3e927055ba09d56bcb632afa0a9fa756209fc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105158219859
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}