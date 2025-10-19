```json
{
  "id": "da799c9224e51169",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285780,
  "host_pid": "9e6742732c60:1",
  "hash": "406538e52bd993e75217c39add0eb4825261ae49e03b5c07312117a242ae8312",
  "cid": "QmV1406538e52bd993e75217c39add0eb4825261ae49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285780,
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
      "evaluated_at": 1760285780
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
  "sig": "176fa0ed55082ad1442021b785bb6e170629c4a7dd57848e5dcd6509cf03a987"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026682072
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}