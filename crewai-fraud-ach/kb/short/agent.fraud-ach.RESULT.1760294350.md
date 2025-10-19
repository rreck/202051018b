```json
{
  "id": "de809a5dcf1c4117",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294350,
  "host_pid": "9e6742732c60:1",
  "hash": "cf6ca2f590befcfe8a590c7a60d7e37213ab3e300e4e06a074d9d1156fb45222",
  "cid": "QmV1cf6ca2f590befcfe8a590c7a60d7e37213ab3e30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294350,
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
      "evaluated_at": 1760294350
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
  "sig": "0b27b73aad866b90bc5556394b977fd82ee7ea34a26180c915ec268173360d58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593870321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 19416900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'ac61827ecd1197f0'}}}