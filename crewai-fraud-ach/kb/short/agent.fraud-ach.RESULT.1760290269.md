```json
{
  "id": "e2bb3375a4764462",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290269,
  "host_pid": "9e6742732c60:1",
  "hash": "95165ef7ea6c6896c9a40457e3e6c5643e57d7c6021d7f77ee7b3120ebb288f7",
  "cid": "QmV195165ef7ea6c6896c9a40457e3e6c5643e57d7c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290269,
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
      "evaluated_at": 1760290269
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
  "sig": "7e0a2c14f9dad9073aace66706807037f0a518ff96a37f62ee5683a622bb2095"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027294403
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 29164668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}