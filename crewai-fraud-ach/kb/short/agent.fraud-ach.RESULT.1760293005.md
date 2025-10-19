```json
{
  "id": "0aa8305ac2906664",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293005,
  "host_pid": "9e6742732c60:1",
  "hash": "254882e81d725a6c4a5c34abdb560a64f2717b1b88e255a17a8555021e5f9da4",
  "cid": "QmV1254882e81d725a6c4a5c34abdb560a64f2717b1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293005,
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
      "evaluated_at": 1760293005
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
  "sig": "859f66842d2f94f2bf04be3ea2bf1f51554df21ffe111c6e5654cae05563c7f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 66513832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}