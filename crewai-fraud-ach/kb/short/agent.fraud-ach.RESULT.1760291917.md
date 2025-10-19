```json
{
  "id": "544cfc357148b4bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291917,
  "host_pid": "9e6742732c60:1",
  "hash": "58caa35e2254dfca4f98488f86f7701b0aa7888e9c7b0daadf37e27ede93f1cf",
  "cid": "QmV158caa35e2254dfca4f98488f86f7701b0aa7888e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291917,
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
      "evaluated_at": 1760291917
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
  "sig": "ea74947cb484238b1bc06571d03f8df63e5a7686dec22929051500bac5b55c27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 23441022, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}