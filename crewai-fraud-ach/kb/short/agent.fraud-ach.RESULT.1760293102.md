```json
{
  "id": "593e9a13b3f7ac4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293102,
  "host_pid": "9e6742732c60:1",
  "hash": "19e3c68a15e4659fcde3a867fa423a4eb43a159769a32ca919b1dcb8299b3a37",
  "cid": "QmV119e3c68a15e4659fcde3a867fa423a4eb43a1597",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293102,
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
      "evaluated_at": 1760293102
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
  "sig": "db531919424aa6613664ba69cb032d5a4ce29b04834073132e272892e489c09a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 67150328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}