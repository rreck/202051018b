```json
{
  "id": "bf6859e9f628bc3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293127,
  "host_pid": "9e6742732c60:1",
  "hash": "5506add896262750f83d02c5eed8ba4d0171b95cea855088f04c3168095e3916",
  "cid": "QmV15506add896262750f83d02c5eed8ba4d0171b95c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293127,
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
      "evaluated_at": 1760293127
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
  "sig": "a32f9fbcd6f127faadf3ef8bd1d4fff5d1f46856a43d8b7d758d59726772283b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466771941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 78013668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'aa929aac6878f78f'}}}