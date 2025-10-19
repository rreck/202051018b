```json
{
  "id": "6193680bd007a30b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290772,
  "host_pid": "9e6742732c60:1",
  "hash": "c01ed821f3dc716600e507e2144075eaf11c9beb35a6d87be191685796184c07",
  "cid": "QmV1c01ed821f3dc716600e507e2144075eaf11c9beb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290772,
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
      "evaluated_at": 1760290772
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
  "sig": "1973903075d45600f5c61d79640b8cc1dbf29111b1c82b0e6124ec76d67f4718"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 60643554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}