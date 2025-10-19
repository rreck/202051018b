```json
{
  "id": "7b12b8dbf09696f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292796,
  "host_pid": "9e6742732c60:1",
  "hash": "ba91b911b88d0709c6d6568f3524954fe79c94b6132542268eda57c2ddd7a9cb",
  "cid": "QmV1ba91b911b88d0709c6d6568f3524954fe79c94b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292796,
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
      "evaluated_at": 1760292796
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
  "sig": "6847f7605232b159f217705ed0e131c777d70228eb0843a94fcb4c2c868b9c79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 281, 'threshold': 50, 'total_amount': 114194185, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 280, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}