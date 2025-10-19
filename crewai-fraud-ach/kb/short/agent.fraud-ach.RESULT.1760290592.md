```json
{
  "id": "c8c779e32a17f8ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290592,
  "host_pid": "9e6742732c60:1",
  "hash": "b7f5e400f6bfc3ea1c77d0a8bf8b01f8b3b331a4b93387521373b2711a513820",
  "cid": "QmV1b7f5e400f6bfc3ea1c77d0a8bf8b01f8b3b331a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290592,
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
      "evaluated_at": 1760290593
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
  "sig": "6861d8add10053b9ec43ca76228f1f2a02bffad51d06794a1bbafe11b2237785"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 41894930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}