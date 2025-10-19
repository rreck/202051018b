```json
{
  "id": "b2efcb07f644a3e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294361,
  "host_pid": "9e6742732c60:1",
  "hash": "90a018cba6e333c32003b32e8657d6cd507c737c0639b78759bd8ce531f561ad",
  "cid": "QmV190a018cba6e333c32003b32e8657d6cd507c737c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294361,
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
      "evaluated_at": 1760294361
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
  "sig": "fefa871e949edfbe34c74339f61700c6a9bcc9a36210278e13994fb15e7fbcb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 95252904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}