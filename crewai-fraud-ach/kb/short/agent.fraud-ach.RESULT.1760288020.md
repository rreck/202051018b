```json
{
  "id": "3f86080607d1888e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288020,
  "host_pid": "9e6742732c60:1",
  "hash": "e77630c7e2f1a10e004735235a1ba99b08c8f3f0fc18d4ec757741be6cfdf1ab",
  "cid": "QmV1e77630c7e2f1a10e004735235a1ba99b08c8f3f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288020,
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
      "evaluated_at": 1760288020
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
  "sig": "b437e5995aca35e3f05d2755e3ca5aaabfc9ec8814842547df0c62e04ebd077f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273941483
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 25052800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '33ec4b85754ad38a'}}}