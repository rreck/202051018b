```json
{
  "id": "0571d6667ad8bfab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294014,
  "host_pid": "9e6742732c60:1",
  "hash": "8bc0fa47f4089c8bdb4c0ecbd2f78cdce66fb7511cc8ae8d591205f3567a268c",
  "cid": "QmV18bc0fa47f4089c8bdb4c0ecbd2f78cdce66fb751",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294014,
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
      "evaluated_at": 1760294014
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
  "sig": "dbcf9bd399429e4050631d811f035168ca7650242b776920555645c74a2cb0f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154917617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 96765830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'bb8a68e9925b6436'}}}