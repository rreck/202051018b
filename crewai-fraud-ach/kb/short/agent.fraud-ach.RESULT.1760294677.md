```json
{
  "id": "a2dacc0e5c0a89a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294677,
  "host_pid": "9e6742732c60:1",
  "hash": "c262de6764acd9e7e8a1029c4d0d8b208cefb3eda30c8cc1ef304b2a26581dad",
  "cid": "QmV1c262de6764acd9e7e8a1029c4d0d8b208cefb3ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294677,
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
      "evaluated_at": 1760294677
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
  "sig": "e3448179c8362647c1b2e80f254caebd9d6b6a2e629eaac995a5442d6f5ac8e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 48849636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}