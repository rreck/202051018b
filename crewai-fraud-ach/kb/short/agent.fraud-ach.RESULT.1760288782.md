```json
{
  "id": "56fe334680a6915b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288782,
  "host_pid": "9e6742732c60:1",
  "hash": "efdf5fe33c846368b4f896cab4ebdeff983aeca752f72f6d835a257f3e5e849e",
  "cid": "QmV1efdf5fe33c846368b4f896cab4ebdeff983aeca7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288782,
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
      "evaluated_at": 1760288782
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
  "sig": "1d5644439f85cf91b23514b9c3f1f679e920ab7e5096b05150ade1255d311d72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023218255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}een': 1760285763, 'matching_hash': '530c0ede13f83176'}}}