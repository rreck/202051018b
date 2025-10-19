```json
{
  "id": "357c84de4ba3b405",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293589,
  "host_pid": "9e6742732c60:1",
  "hash": "8fb571aa595438dc81fe95bca747c42bd89741a01fef9fb9186ea561a2067551",
  "cid": "QmV18fb571aa595438dc81fe95bca747c42bd89741a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293589,
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
      "evaluated_at": 1760293589
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
  "sig": "240495bb542f4f87340dc81a60fb15696bdc70eae1276481ec2e2979e854ab1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 109007587, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}