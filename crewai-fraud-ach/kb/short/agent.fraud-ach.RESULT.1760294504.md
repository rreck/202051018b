```json
{
  "id": "35e651e0fca91d8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294504,
  "host_pid": "9e6742732c60:1",
  "hash": "22dd848230fdc5e513dd4228ebcad1e585e32ebc77f7d3e6c8b806eb5d20bec1",
  "cid": "QmV122dd848230fdc5e513dd4228ebcad1e585e32ebc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294504,
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
      "evaluated_at": 1760294504
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
  "sig": "1dc63c4b0fc5320f56c301c49df9bd36e946ca5fb0174a938d7de1a140830d88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026494478
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 45294563, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'bca1271a1f86b87c'}}}