```json
{
  "id": "c7c7e95c9cc9f86a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294878,
  "host_pid": "9e6742732c60:1",
  "hash": "9c578afa4eaf71a55ca1ad53b76b76126300c33b9d7848dc217e464ed0bd3d92",
  "cid": "QmV19c578afa4eaf71a55ca1ad53b76b76126300c33b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294878,
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
      "evaluated_at": 1760294878
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
  "sig": "b130da2806cc385ff13ddb9b18feecd9266963d2b5c7345918ca6eed9a102adb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 66035994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}