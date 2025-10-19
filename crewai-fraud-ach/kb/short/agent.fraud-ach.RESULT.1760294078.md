```json
{
  "id": "c0c494ac6e56fc1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294078,
  "host_pid": "9e6742732c60:1",
  "hash": "13ce8ba83bb679a237aae30a42eadd286397edac17f0c489d6812e7e08a6beb9",
  "cid": "QmV113ce8ba83bb679a237aae30a42eadd286397edac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294078,
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
      "evaluated_at": 1760294078
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
  "sig": "2ed25115845f22da52dbc5ea8c6c8846044f46d71538072e5180ef28bfab25d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157479316
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 27048252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': 'd3845a7ded8f78ea'}}}