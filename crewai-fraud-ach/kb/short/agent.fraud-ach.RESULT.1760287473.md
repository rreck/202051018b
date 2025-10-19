```json
{
  "id": "eb3f5a6d32baec3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287473,
  "host_pid": "9e6742732c60:1",
  "hash": "639ad1f42b8f7da70387096382428e0141e84173f8ca3762ccd6e5d6a34bcc69",
  "cid": "QmV1639ad1f42b8f7da70387096382428e0141e84173",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287473,
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
      "evaluated_at": 1760287473
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
  "sig": "da7be36ed052663edf7b24c74a8fca4347ee591c2a6ff525bfd94b5f8237a0a7"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 23650005, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}