```json
{
  "id": "2600d541a686ccb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294759,
  "host_pid": "9e6742732c60:1",
  "hash": "574cd835b4ee15652b8e5d97691077da8974dd7f85199a08f310a1006537d21f",
  "cid": "QmV1574cd835b4ee15652b8e5d97691077da8974dd7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294759,
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
      "evaluated_at": 1760294759
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
  "sig": "143e6868ef0c0e776760528f939719dcc801a4fa4f2ba1c0e54211ea40986796"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028760265
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 67814920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'ff1172b8afcaa4bc'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}