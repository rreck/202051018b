```json
{
  "id": "4ac433c0f8cd5af5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289793,
  "host_pid": "9e6742732c60:1",
  "hash": "cbeb364449c9a3e15a90770b04d8bd49c8269641236000f0f6abe640de8c296f",
  "cid": "QmV1cbeb364449c9a3e15a90770b04d8bd49c8269641",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289793,
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
      "evaluated_at": 1760289793
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
  "sig": "14bc58bf902fc8771b0e95d94ef3515cccb4ef39054c4c7e8dace859534e7a3c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467602006
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 61715059, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': 'cc8ab13ff4b154cd'}}}