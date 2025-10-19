```json
{
  "id": "e3cf3f3ff1453b8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291022,
  "host_pid": "9e6742732c60:1",
  "hash": "6cde2fc3263e8923a1e1211ea5dbbe59dc5b6156b4cf35c94da198144fd82b20",
  "cid": "QmV16cde2fc3263e8923a1e1211ea5dbbe59dc5b6156",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291022,
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
      "evaluated_at": 1760291022
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
  "sig": "0db8a88a57c4b2a7dce834752165fb59099eefd83bdf574980b1b390a63ad6f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 72548850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}