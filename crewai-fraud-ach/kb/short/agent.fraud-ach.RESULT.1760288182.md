```json
{
  "id": "006d1cb328213788",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288182,
  "host_pid": "9e6742732c60:1",
  "hash": "24b18dafd7094dcf5334f1b62774886a63e45b96b4171d8e901676a83aa05a2a",
  "cid": "QmV124b18dafd7094dcf5334f1b62774886a63e45b96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288182,
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
      "evaluated_at": 1760288182
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
  "sig": "ab121cde4d07cbfd2dd0b5dc5ebba12f554a2f9d357e3aa960c6141a5cd05caa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159090424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 14699645, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285764, 'matching_hash': 'fe78f8ea626833d8'}}}