```json
{
  "id": "9a814e352961ef3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294868,
  "host_pid": "9e6742732c60:1",
  "hash": "4a64b2db5a9092d747adb8715aa76930478e3744e3c7b91abd01e93f13614588",
  "cid": "QmV14a64b2db5a9092d747adb8715aa76930478e3744",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294868,
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
      "evaluated_at": 1760294868
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
  "sig": "d79a3f42f25b47147903be12d7a8bc98714f8dbabea103d57d7bf6e338bf2e2f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151540950
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 47564592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}