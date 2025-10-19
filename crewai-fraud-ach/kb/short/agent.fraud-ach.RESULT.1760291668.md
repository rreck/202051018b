```json
{
  "id": "9adde5f570c0d4bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291668,
  "host_pid": "9e6742732c60:1",
  "hash": "265b0300b0cf3f80339ad6053602f9612bfd72437cea1fa44413c4e7187cb91d",
  "cid": "QmV1265b0300b0cf3f80339ad6053602f9612bfd7243",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291668,
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
      "evaluated_at": 1760291668
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
  "sig": "acbf8ac77785a4d0168c5b952d1c903244d6395d010cefa6d45bb5c0f47d53f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023479394
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 70771680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '601e7e272d8441f2'}}}