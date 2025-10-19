```json
{
  "id": "fd349cbcc38cb5c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292575,
  "host_pid": "9e6742732c60:1",
  "hash": "929f5403958b588a857c4aba77a58d5b02b99e221cd81356e38523163db8d184",
  "cid": "QmV1929f5403958b588a857c4aba77a58d5b02b99e22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292575,
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
      "evaluated_at": 1760292575
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
  "sig": "dacfae41d5b102c8ab2b95bedb776cd7857b56ed5782c244b4b6462dc1cc057c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 33203400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}