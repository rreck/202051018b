```json
{
  "id": "ed7b7965bfc22a32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290206,
  "host_pid": "9e6742732c60:1",
  "hash": "2d1d4fdb08a6c612940d2d9ba1ff99384c4ce1856ff5933f457257e2a0233289",
  "cid": "QmV12d1d4fdb08a6c612940d2d9ba1ff99384c4ce185",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290206,
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
      "evaluated_at": 1760290207
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
  "sig": "8b1c9b59dcb89d4f84774fef32309e012cd5babc646bcee62356f64092d91853"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245381675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 23619024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}