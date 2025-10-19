```json
{
  "id": "b1ae9ffefffe299d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293734,
  "host_pid": "9e6742732c60:1",
  "hash": "9da6fdf36f3368f100793c14029412c5063bbf555d3463d35a7222067d106af0",
  "cid": "QmV19da6fdf36f3368f100793c14029412c5063bbf55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293734,
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
      "evaluated_at": 1760293734
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
  "sig": "890ed7ef6a13625914220db6b09867dfdc0e5596ee70b10e52b4d9e65d9fed14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 100020480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}