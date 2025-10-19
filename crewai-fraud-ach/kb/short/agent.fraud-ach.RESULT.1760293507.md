```json
{
  "id": "81756b8237174d04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293507,
  "host_pid": "9e6742732c60:1",
  "hash": "22a336977d6e1646c04149a4e80daefd6148253978eba4d0f8f4ff9ef1c7a740",
  "cid": "QmV122a336977d6e1646c04149a4e80daefd61482539",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293507,
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
      "evaluated_at": 1760293507
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
  "sig": "f4a0cc2d7f5a2d3dbfb11fb405c7ce359821ecef1464c280b3b0ed3d698e9ec2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 29375940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}