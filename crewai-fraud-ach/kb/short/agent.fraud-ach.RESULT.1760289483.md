```json
{
  "id": "12eee3ea87994903",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289483,
  "host_pid": "9e6742732c60:1",
  "hash": "2d0a11df47f3d2635e9a43ac20626e95b96bb8c938ebe25cea239daba4525303",
  "cid": "QmV12d0a11df47f3d2635e9a43ac20626e95b96bb8c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289483,
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
      "evaluated_at": 1760289483
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
  "sig": "4db25d29497161eabec49dd23fa4bb504827d17ee81957cb04c4e1e896260370"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 53743956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}