```json
{
  "id": "7c2a0e6d52cf1848",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292754,
  "host_pid": "9e6742732c60:1",
  "hash": "53f90058ee4f85adf7fb473265f5bd93ccfafbb48066c00ce07f5228b52f108e",
  "cid": "QmV153f90058ee4f85adf7fb473265f5bd93ccfafbb4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292754,
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
      "evaluated_at": 1760292754
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
  "sig": "84922fc90bb96167b748f44e3f64c2ce2b5364cdb9d72fea922cfc97b2077a71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 90111900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}