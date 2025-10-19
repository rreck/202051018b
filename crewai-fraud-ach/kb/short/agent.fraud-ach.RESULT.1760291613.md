```json
{
  "id": "39b0a4b4451de977",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291613,
  "host_pid": "9e6742732c60:1",
  "hash": "ce6b5b4c87dc30695018781103b225495c8264dfa339aca434ee12896286e90d",
  "cid": "QmV1ce6b5b4c87dc30695018781103b225495c8264df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291613,
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
      "evaluated_at": 1760291613
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
  "sig": "0fe2d9248e79f556466ded80b07778f2441d595e52646d22f2caf7a9cd9a91ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038318648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 57293962, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': '13d51597e8ec53d0'}}}