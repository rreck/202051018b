```json
{
  "id": "36f0db1abc888020",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294398,
  "host_pid": "9e6742732c60:1",
  "hash": "fc76ccffd49c14dc8acbac546e3505b3cdc7c82026bafc83883d485a0998c896",
  "cid": "QmV1fc76ccffd49c14dc8acbac546e3505b3cdc7c820",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294398,
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
      "evaluated_at": 1760294398
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
  "sig": "71770b8204bba2135880dd3c4a1d35bbc80e5d2b6a24dba69185d6c852f1c326"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275777124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 65366022, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'd1e6afcf07f21c4a'}}}}