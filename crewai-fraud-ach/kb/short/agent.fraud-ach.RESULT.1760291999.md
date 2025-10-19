```json
{
  "id": "540e3b39e136a299",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291999,
  "host_pid": "9e6742732c60:1",
  "hash": "583507c9cd618f4ed5b13ded42fe1db42b13320163e28a2c58c00336d75c56fa",
  "cid": "QmV1583507c9cd618f4ed5b13ded42fe1db42b133201",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291999,
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
      "evaluated_at": 1760291999
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
  "sig": "eb93824150f5570e7073fc514c8483a24ea72f1547f39576c2eaa22d892c810c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025380503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 14791088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '5a364e4e5c1e4dba'}}}