```json
{
  "id": "1d05a363f1c4a292",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288705,
  "host_pid": "9e6742732c60:1",
  "hash": "c4b9484433d1fddd309e682b18b26538217f2f164984dfcbe01561fac0d48abd",
  "cid": "QmV1c4b9484433d1fddd309e682b18b26538217f2f16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288705,
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
      "evaluated_at": 1760288705
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
  "sig": "0241b0d7fa864a32da103d0e0b351566758a8d843ea734039c4ead7fca10e6c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 16767717, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}