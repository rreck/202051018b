```json
{
  "id": "775700c7e775b18f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288891,
  "host_pid": "9e6742732c60:1",
  "hash": "99fd502388565c8bb0fffb654dd8b9927e226e4cd2525c41bef2e97d54755ab1",
  "cid": "QmV199fd502388565c8bb0fffb654dd8b9927e226e4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288891,
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
      "evaluated_at": 1760288891
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
  "sig": "b303f0dff5dd1aa66755d46a11dc623698eb2b3baf7894279243117ba067bad7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 48322614, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}