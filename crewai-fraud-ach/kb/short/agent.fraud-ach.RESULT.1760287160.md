```json
{
  "id": "2f81e3d7eb2515d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287160,
  "host_pid": "9e6742732c60:1",
  "hash": "9ade58e3b90670610305bbca758153bc0511ff0882b44de8ae4fb52e95644d2e",
  "cid": "QmV19ade58e3b90670610305bbca758153bc0511ff08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287160,
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
      "evaluated_at": 1760287160
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
  "sig": "f32d893a55c9f25ee1a1e5e7ad67f38537c3e3a935c3713cdce2ef51fb5c463a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12723500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}