```json
{
  "id": "20811b43d7757f67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290733,
  "host_pid": "9e6742732c60:1",
  "hash": "b3355174ab56a864177646f72a7989884b9e2dd2076497823f31fe4f9af2799b",
  "cid": "QmV1b3355174ab56a864177646f72a7989884b9e2dd2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290733,
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
      "evaluated_at": 1760290733
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
  "sig": "d93b44dea2ea118364418d3593524d39fa42810ee85f49f2a8dd4f1764b0d19d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159848459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 32553056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}