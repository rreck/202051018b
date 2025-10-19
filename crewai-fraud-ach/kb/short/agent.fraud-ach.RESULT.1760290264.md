```json
{
  "id": "2b32065dafea864a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290264,
  "host_pid": "9e6742732c60:1",
  "hash": "d629b5a9fb8712ba336572319556d57c26a66d99b0155cbd9762a33f8bc369d1",
  "cid": "QmV1d629b5a9fb8712ba336572319556d57c26a66d99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290264,
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
      "evaluated_at": 1760290264
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
  "sig": "c981c5e4ca113c86f7c4d0be80612ef1ba7d830edf01290d640d40ef68d23083"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460250809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 61468628, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}