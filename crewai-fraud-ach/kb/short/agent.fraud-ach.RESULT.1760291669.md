```json
{
  "id": "5ea94eceb57c4025",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291669,
  "host_pid": "9e6742732c60:1",
  "hash": "6b45f3a271417bfe44be417f3bb592acb73af95c366bab5cb347c68eeebdc701",
  "cid": "QmV16b45f3a271417bfe44be417f3bb592acb73af95c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291669,
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
      "evaluated_at": 1760291669
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
  "sig": "77d1ba17bac173c370cb0e647e0fdf4f6d995d75a71022909b24bdf1ef147f84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462554282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 10482120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}