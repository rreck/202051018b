```json
{
  "id": "fe5561b034e9b757",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293441,
  "host_pid": "9e6742732c60:1",
  "hash": "062de93bb648605bec4acb932e54e3c8b9fda80f370378427127c15d526a3c83",
  "cid": "QmV1062de93bb648605bec4acb932e54e3c8b9fda80f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293441,
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
      "evaluated_at": 1760293441
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
  "sig": "7471f1bc0b4d3f44fe41794c21fc1a705d3dcf73f4945673829be5930380f768"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 69378064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}