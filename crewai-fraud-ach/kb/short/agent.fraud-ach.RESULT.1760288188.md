```json
{
  "id": "59bd08a5fa0982e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288188,
  "host_pid": "9e6742732c60:1",
  "hash": "595ac503ad07bddb76110e9f06e921fce3e8e5dba9534fecf9c0c5387d049cb2",
  "cid": "QmV1595ac503ad07bddb76110e9f06e921fce3e8e5db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288188,
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
      "evaluated_at": 1760288188
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
  "sig": "9ee8de2b8e507ff29bef3690a608aee93c96dc20e488e53f5dc02dabe2b9110c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 20798650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}