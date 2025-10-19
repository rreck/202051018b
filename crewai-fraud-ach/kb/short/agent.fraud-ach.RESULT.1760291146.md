```json
{
  "id": "0d9d122911a4104b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291146,
  "host_pid": "9e6742732c60:1",
  "hash": "12b1c2c77e663fd1df461c447b0d6ccbf618fc6701d170ee0c6b4922116c3f57",
  "cid": "QmV112b1c2c77e663fd1df461c447b0d6ccbf618fc67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291146,
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
      "evaluated_at": 1760291146
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
  "sig": "762032ccc077f63a698cf10c1230dc44b7e6532e24ff6be81bd09fdfa216536d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024763111
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 33751704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': '9fa093ca4f14e7a1'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}