```json
{
  "id": "0c189e708691d795",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286150,
  "host_pid": "9e6742732c60:1",
  "hash": "2d02730557991be3833ec7a6211a71acb9dbdfd6c82566498b924552afb46a31",
  "cid": "QmV12d02730557991be3833ec7a6211a71acb9dbdfd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286150,
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
      "evaluated_at": 1760286150
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
  "sig": "73880dec13f1d674c724084e00406d7dc905af0cb07379629e5949e80ab23614"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024843981
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285764, 'matching_hash': 'a5434e6981d8724b'}}}