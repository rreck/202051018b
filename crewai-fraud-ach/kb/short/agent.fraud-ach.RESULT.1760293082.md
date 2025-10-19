```json
{
  "id": "3279e527c93991bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293082,
  "host_pid": "9e6742732c60:1",
  "hash": "7cffb61b27e29ce4456596ba2c6568ff94d9365a5fd39aba947e627a1c50f998",
  "cid": "QmV17cffb61b27e29ce4456596ba2c6568ff94d9365a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293082,
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
      "evaluated_at": 1760293082
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
  "sig": "a81b076f2c7197447fbddba1733f67c2b20dcbc7ddfcbd69e9377050246e76ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 62885174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}