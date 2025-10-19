```json
{
  "id": "68cf6fbb16902ac7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287471,
  "host_pid": "9e6742732c60:1",
  "hash": "ef5fecadff04e64fc27637494ff51c0e1d47c405491066e87112c303baf225f5",
  "cid": "QmV1ef5fecadff04e64fc27637494ff51c0e1d47c405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287471,
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
      "evaluated_at": 1760287471
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
  "sig": "827e673b10a69927ba54e575ae452ce6d8caf064527a2394c2eff37bbadd427d"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 23924200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}