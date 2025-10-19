```json
{
  "id": "4f24d2126e177254",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286729,
  "host_pid": "9e6742732c60:1",
  "hash": "9fa7f66efda2f1ad128c06e20e2ac2d0f6f4f280b4e8f3e20ebc6d0795708096",
  "cid": "QmV19fa7f66efda2f1ad128c06e20e2ac2d0f6f4f280",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286729,
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
      "evaluated_at": 1760286729
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "dc48f9bd3872fec0ac7ec8503e480df30e3edb964fdaf7d7e1ed11c136a34fa8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10272780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}