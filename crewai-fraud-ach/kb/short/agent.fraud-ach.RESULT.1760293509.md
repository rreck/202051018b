```json
{
  "id": "1f305724846ac961",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293509,
  "host_pid": "9e6742732c60:1",
  "hash": "1574661ea71757c7a63533f380b51693077b59a0d7bfb345c55ebf087dedf5f6",
  "cid": "QmV11574661ea71757c7a63533f380b51693077b59a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293509,
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
      "evaluated_at": 1760293509
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
  "sig": "d514cb0a5b0c5162e1b35395f1b82861fc800f42ca0df4168fcfe52eba1b210c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592648645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 83205540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'd7971b176fb0516b'}}}