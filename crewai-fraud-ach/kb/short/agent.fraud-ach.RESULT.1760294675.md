```json
{
  "id": "629ea5f189929f2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294675,
  "host_pid": "9e6742732c60:1",
  "hash": "1ff1d7126f13dcb465a84e8432bb53a1dc3f4590f64caf3687ceb217d2633b72",
  "cid": "QmV11ff1d7126f13dcb465a84e8432bb53a1dc3f4590",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294675,
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
      "evaluated_at": 1760294675
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
  "sig": "39027a69ea8d3d6433242bd5a228c1118aa681a126cfb05542bf50ad068bf0c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036177444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 42826498, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}