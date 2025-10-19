```json
{
  "id": "d9bd2b794232df9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292747,
  "host_pid": "9e6742732c60:1",
  "hash": "52bd8ac55c2a18fffb9cdf3456fdb8ca169a27cfe2622c411bd5d4da8ec90cfa",
  "cid": "QmV152bd8ac55c2a18fffb9cdf3456fdb8ca169a27cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292747,
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
      "evaluated_at": 1760292747
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
  "sig": "8c3d1875ac9c4bada6d24f35899921e18ccf863cb0255303f8ad801e1282043e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270359022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 45584412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}