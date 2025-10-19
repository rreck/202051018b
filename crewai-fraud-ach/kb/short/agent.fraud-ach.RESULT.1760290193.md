```json
{
  "id": "aba513217ee253b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290193,
  "host_pid": "9e6742732c60:1",
  "hash": "b5b52a99450d3d879fb88c4a7c62485aa02ab49052509c4329d9babd87adbd42",
  "cid": "QmV1b5b52a99450d3d879fb88c4a7c62485aa02ab490",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290193,
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
      "evaluated_at": 1760290193
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
  "sig": "986fccfd8e8369dce97b101225f051511a4ffcb7fc497dc85da5a77abaf54258"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596116036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 36000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': 'e2bf4d89584c6445'}}}