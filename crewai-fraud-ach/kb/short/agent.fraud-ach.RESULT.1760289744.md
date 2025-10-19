```json
{
  "id": "7805dd1a589df346",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289744,
  "host_pid": "9e6742732c60:1",
  "hash": "68abc1bfe083cb6fd916bdb0e4a20dd31e14385de80a970953ad7f1e34f23d44",
  "cid": "QmV168abc1bfe083cb6fd916bdb0e4a20dd31e14385d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289744,
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
      "evaluated_at": 1760289744
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
  "sig": "bad6fdc3f8801faa14ba6f470a38d84721b48d3a3b07487adbbbef450da4641b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035593386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 15754860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '6253d15ae41563d2'}}}