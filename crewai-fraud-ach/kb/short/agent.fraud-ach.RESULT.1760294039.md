```json
{
  "id": "c0106cab0f553508",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294039,
  "host_pid": "9e6742732c60:1",
  "hash": "d84babe1ffb75fa71476b9ccd3b7f7acad3e18bea49f782bc35d30d4fb0ef01f",
  "cid": "QmV1d84babe1ffb75fa71476b9ccd3b7f7acad3e18be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294039,
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
      "evaluated_at": 1760294039
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
  "sig": "a029d519a2b2d317053c72abf3abb4ce9920d3302cd568147405a640f6280e33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 58528100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}