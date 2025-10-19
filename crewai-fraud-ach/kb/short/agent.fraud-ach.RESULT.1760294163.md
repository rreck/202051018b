```json
{
  "id": "0c6cf8a16bb5a1ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294163,
  "host_pid": "9e6742732c60:1",
  "hash": "bdb34c5db497bea007800ba07cbdacd4b7192ce21d6e27570fa292d1eece9b3e",
  "cid": "QmV1bdb34c5db497bea007800ba07cbdacd4b7192ce2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294163,
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
      "evaluated_at": 1760294163
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
  "sig": "89905df1882a85b6cd55aba84e02feb4c068adf05f54170f5daa0bcad27b0bb8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590985666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 46660347, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': 'a91912abaf20cb4f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}