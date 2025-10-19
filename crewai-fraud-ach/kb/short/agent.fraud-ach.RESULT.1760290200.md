```json
{
  "id": "0f775010e6acb92b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290200,
  "host_pid": "9e6742732c60:1",
  "hash": "5b6b7565ba22ad8074d58a9c08e09b125a437982f362ac1f5a6558a2199909be",
  "cid": "QmV15b6b7565ba22ad8074d58a9c08e09b125a437982",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290200,
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
      "evaluated_at": 1760290200
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
  "sig": "fb5b3bed63466d7aadec2683a62f579fdebcdd90c4dfaec43f0c43b79b029a37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154971432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 48719664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': 'db584ac34c85fc07'}}}