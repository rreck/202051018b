```json
{
  "id": "530f2eec7edcf603",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293655,
  "host_pid": "9e6742732c60:1",
  "hash": "f59ab91195208bc2042dd34682695cbb0c850f54690f9b4081a753cf0132441d",
  "cid": "QmV1f59ab91195208bc2042dd34682695cbb0c850f54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293655,
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
      "evaluated_at": 1760293655
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
  "sig": "a57598b35efa108f329e8173a05ba1202d986fcfa4f5fdf5268c3ab5b1ce4d59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 38797540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}