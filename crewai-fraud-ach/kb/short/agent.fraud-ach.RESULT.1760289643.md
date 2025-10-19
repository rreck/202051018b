```json
{
  "id": "ade0cde880b73de1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289643,
  "host_pid": "9e6742732c60:1",
  "hash": "f715195c6ffbb7ec3e6a56fed4fdcd0f658d4ea36d2cda057fed78033dd04e14",
  "cid": "QmV1f715195c6ffbb7ec3e6a56fed4fdcd0f658d4ea3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289643,
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
      "evaluated_at": 1760289643
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
  "sig": "91958a359efb317a9aee299251b28d58172eb640ca2f4fabb59be6d485bc4033"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032976698
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 47901957, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': 'b86b53820ba813a1'}}}